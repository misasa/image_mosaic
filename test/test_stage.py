import sys
import os
import shutil
from nose.tools import *
from image_mosaic.stage import *

files_dir = os.path.join(os.path.dirname(__file__), 'files')
saved = None

def setup_tmp():
  if os.path.exists('tmp'):
    shutil.rmtree('tmp')
  os.mkdir('tmp')

def setup():
  setup_tmp()
  global saved
  saved = sys.argv

def teardown():
  sys.argv = saved

@with_setup(setup, teardown)
def test_main():
  shutil.copy(os.path.join(files_dir, 'cat.jpg'),'tmp')
  stage = Stage()
  stage.set_image('tmp/cat.jpg', numpy.array([[1,0,0],[0,1,0],[0,0,1]]))