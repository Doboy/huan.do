#!/usr/bin/env python

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def main():
  gauth = GoogleAuth()
  gauth.LocalWebserverAuth()

  drive = GoogleDrive(gauth)

  file_list = drive.ListFile({'q': "title = 'Resume' and trashed = false"}).GetList()
  assert len(file_list) == 1, file_list
  resume_file = file_list[0]
  resume_file.GetContentFile('resume.pdf', mimetype='application/pdf')

if __name__ == '__main__':
  main()
