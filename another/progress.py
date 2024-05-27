import time
from tqdm import tqdm,trange
from rich.progress import track,Progress
import urllib.request

# for i in tqdm(range(100),desc="Training",unit="epoch"):
#     time.sleep(0.1)

# for i in trange(100,desc="Training",unit="epoch"):
#     time.sleep(0.1)

# for i in track(range(100),description="进度",complete_style="green",finished_style="blue"):
#     url=f"xxxx{i}.tar.gz"
#     print(url)
#     # content=urllib.request.urlopen(url).read()
#     # with open(f"./{i}.tar.gz",'wb') as f:
#     #     f.write(content)
#     time.sleep(0.1)              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
with Progress() as progress:
    task1=progress.add_task("[red]下载...",total=10)
    task2=progress.add_task("[green]处理...",total=10)
    task3=progress.add_task("[yellow]保存...",total=10)
    while not progress.finished:
        progress.update(task1,advance=0.5)
        progress.update(task2,advance=0.2)
        progress.update(task3,advance=1)
        time.sleep(1)
