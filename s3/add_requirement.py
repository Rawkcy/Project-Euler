#! /usr/bin/env python
import os, sys, shutil
from waveaccounting import settings

class addNewRequirement(object):
    def __init__(self, package, version):
        self.package = package
        self.version = version
        self.package_download_dir = "tarball_pkgs"
        self.package_requirement = "%s==%s" % (self.package, self.version)
        self.web_page = "libs_index.html"

    def push_to_s3_repo(self, file_name):
        """Push given file to s3 repo"""
        os.system("s3put -a %s -s %s -b waveaccounting-libs %s" % (settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY, file_name))

    def create_temp_download_dir(self):
        """Create a directory for the tarballs"""
        os.mkdir(self.package_download_dir)

    def download_tarball(self):
        """Download tarball to folder using pip"""
        try:
            os.system("pip install --timeout=60 -d %s/ %s" % (self.package_download_dir, self.package_requirement))
        except:
            sys.exit("Unable to download %s" % self.package_requirement)

    def add_package_download_to_list_of_requirements(self):
        """Add the package name to list of custom requirements"""
        with open("custom_requirements.pip", "a") as custom_requirements:
            custom_requirements.write("%s\n" % self.package_requirement)
        print "Successfully added %s to custom_requirements.pip" % self.package_requirement

    def get_package_name(self):
        """Assume package is tarball unless it doesn't exist in which case we switch extension to .zip"""
        package = "%s-%s.tar.gz" % (self.package, self.version)

        #is_tarball = os.path.exists("%s/%s" % (self.package_download_dir, package))
        #if not is_tarball:
        #    package = package.replace(".tar.gz", ".zip")
        #return package

        import fnmatch
        for file in os.listdir('%s' % self.package_download_dir):
            if fnmatch.fnmatch(file, '*.zip'):
                package = package.replace(".tar.gz", ".zip")
        return package


    def add_package_name_to_webpage(self, package):
        """Append the link of new package to the end of the webpage"""
        html_link = "<li><a href=\"%s\">%s</a></li>\n" % (package, package)
        with open(self.web_page, "a") as web_page:
            web_page.write(html_link)

    def upload_files_to_s3(self, package):
        """Upload requirement package and web page to s3"""
        try:
            # Push package to s3 while inside the download folder
            os.chdir(self.package_download_dir)
            self.push_to_s3_repo(package)
            print "Successfully uploaded %s" % package
            os.chdir("..")
            # Push updated web page to s3
            self.push_to_s3_repo(self.web_page)
            print "Successfully uploaded %s" % self.web_page
        except:
            print "Failed to uplaod %s" % package

    def remove_temp_download_dir(self):
        """Remove temporary package download folder"""
        shutil.rmtree(self.package_download_dir)

    def add_package_and_upload_to_s3(self):
        """Add package version to list of requirements and package anme to webpage then upload files to s3 repo"""
        self.add_package_download_to_list_of_requirements()

        requirement_filename = self.get_package_name()
        self.add_package_name_to_webpage(requirement_filename)
        self.upload_files_to_s3(requirement_filename)

    def add_package_requirement_to_repo(self):
        self.create_temp_download_dir()
        self.download_tarball()
        self.add_package_and_upload_to_s3()
        self.remove_temp_download_dir()

    def install_requirements(self):
        os.system("pip install -r custom_requirements.pip")

if __name__== "__main__":
    if len(sys.argv) != 3:  # The program name and two arguments
        sys.exit("Please only provide the package name and package version")
    package = sys.argv[1]
    version = sys.argv[2]

    requirements_helper = addNewRequirement(package, version)
    requirements_helper.add_package_requirement_to_repo()
    requirements_helper.install_requirements()
