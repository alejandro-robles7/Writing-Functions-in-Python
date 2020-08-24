import contextlib
import time
import numpy as np


def _process_pic(n_sec):
    print('Processing', end='', flush=True)
    for i in range(10):
        print('.', end='' if i < 9 else 'done!\n', flush=True)
        time.sleep(n_sec)


def process_with_numpy(p):
    _process_pic(0.1521)


def process_with_pytorch(p):
    _process_pic(0.0328)


def get_image_from_instagram():
    return np.random.rand(84, 84)


@contextlib.contextmanager
def timer():
  """Time how long code in the context block takes to run."""
  t0 = time.time()
  try:
      yield
  except:
    raise
  finally:
    t1 = time.time()
    print('Elapsed: {:.2f} seconds'.format(t1 - t0))