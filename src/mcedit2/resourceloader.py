"""
    ${NAME}
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import logging
import zipfile

log = logging.getLogger(__name__)

class ResourceNotFound(KeyError):
    pass

class ResourceLoader(object):
    def __init__(self):
        super(ResourceLoader, self).__init__()
        self.zipFiles = []

    def addZipFile(self, zipPath):
        try:
            zf = zipfile.ZipFile(zipPath)
        except zipfile.BadZipfile as e:
            raise IOError("Could not read %s as a zip file." % zipPath)
        self.zipFiles.append(zf)

    def openStream(self, path):
        path = "assets/minecraft/%s" % path

        for zipFile in self.zipFiles:
            try:
                stream = zipFile.open(path)
                break
            except KeyError:  # Not found in zip file
                continue
        else:
            raise ResourceNotFound("Resource %s not found in search path" % path)

        return stream
