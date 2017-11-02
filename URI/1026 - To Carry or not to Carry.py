def Main(a, b):
  print(a^b)
if __name__ == '__main__':
  while True:
    try:
      a, b = map(int ,input().split())
    except EOFError:
      break
    Main(a, b)