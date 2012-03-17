#
# Copyright [2012] [Ali Ok - aliok@apache.org]
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

__author__ = 'ali'

import sys
import shutil
import os

def main():
    pagesSourceFolder = '../generated-pages/pages/'
    pagesDestinationFolder = 'pages/'
    resourcesSourceFolder = '../web-resources/resources/'
    resourcesDestinationFolder = 'resources/'

    if not os.path.exists(pagesSourceFolder):
        print('Pages source folder "{0}" does not exist!'.format(pagesSourceFolder))
        return -1

    if not os.path.exists(resourcesSourceFolder):
        print('Resources source folder "{0}" does not exist!'.format(resourcesSourceFolder))
        return -1

    print 'Deleting pages destionation folder "{0}"'.format(pagesDestinationFolder)
    if os.path.exists(pagesDestinationFolder):
        shutil.rmtree(pagesDestinationFolder)

    print 'Copying pages from "{0}" to "{1}"'.format(pagesSourceFolder, pagesDestinationFolder)
    shutil.copytree(pagesSourceFolder, pagesDestinationFolder)

    print 'Deleting resources destination folder "{0}"'.format(resourcesDestinationFolder)
    if os.path.exists(resourcesDestinationFolder):
        shutil.rmtree(resourcesDestinationFolder)

    print 'Copying pages from "{0}" to "{1}"'.format(resourcesSourceFolder, resourcesDestinationFolder)
    shutil.copytree(resourcesSourceFolder, resourcesDestinationFolder)

if __name__ == "__main__":
    sys.exit(main())