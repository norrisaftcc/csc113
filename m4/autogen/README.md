# notes on autogen

# Mallory's sample run
@milsteam4144 ➜ /workspaces/CTI-110 (main) $ pip install autogen

Collecting autogen
  Downloading autogen-1.0.16-py3-none-any.whl.metadata (292 bytes)
Requirement already satisfied: PyYAML in /home/codespace/.local/lib/python3.10/site-packages (from autogen) (6.0.1)
Collecting autopep8 (from autogen)
  Downloading autopep8-2.1.0-py2.py3-none-any.whl.metadata (16 kB)
Collecting docopt (from autogen)
  Downloading docopt-0.6.2.tar.gz (25 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: setuptools in /usr/local/python/3.10.13/lib/python3.10/site-packages (from autogen) (68.2.2)
Collecting twine (from autogen)
  Downloading twine-5.0.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pycodestyle>=2.11.0 (from autopep8->autogen)
  Downloading pycodestyle-2.11.1-py2.py3-none-any.whl.metadata (4.5 kB)
Requirement already satisfied: tomli in /home/codespace/.local/lib/python3.10/site-packages (from autopep8->autogen) (2.0.1)
Collecting pkginfo>=1.8.1 (from twine->autogen)
  Downloading pkginfo-1.10.0-py3-none-any.whl.metadata (11 kB)
Collecting readme-renderer>=35.0 (from twine->autogen)
  Downloading readme_renderer-43.0-py3-none-any.whl.metadata (2.8 kB)
Requirement already satisfied: requests>=2.20 in /home/codespace/.local/lib/python3.10/site-packages (from twine->autogen) (2.31.0)
Collecting requests-toolbelt!=0.9.0,>=0.8.0 (from twine->autogen)
  Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
Requirement already satisfied: urllib3>=1.26.0 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from twine->autogen) (2.0.7)
Collecting importlib-metadata>=3.6 (from twine->autogen)
  Downloading importlib_metadata-7.1.0-py3-none-any.whl.metadata (4.7 kB)
Collecting keyring>=15.1 (from twine->autogen)
  Downloading keyring-25.0.0-py3-none-any.whl.metadata (20 kB)
Collecting rfc3986>=1.4.0 (from twine->autogen)
  Downloading rfc3986-2.0.0-py2.py3-none-any.whl.metadata (6.6 kB)
Collecting rich>=12.0.0 (from twine->autogen)
  Downloading rich-13.7.1-py3-none-any.whl.metadata (18 kB)
Collecting zipp>=0.5 (from importlib-metadata>=3.6->twine->autogen)
  Downloading zipp-3.18.1-py3-none-any.whl.metadata (3.5 kB)
Collecting jaraco.classes (from keyring>=15.1->twine->autogen)
  Downloading jaraco.classes-3.3.1-py3-none-any.whl.metadata (2.7 kB)
Collecting jaraco.functools (from keyring>=15.1->twine->autogen)
  Downloading jaraco.functools-4.0.0-py3-none-any.whl.metadata (3.1 kB)
Collecting jaraco.context (from keyring>=15.1->twine->autogen)
  Downloading jaraco.context-4.3.0-py3-none-any.whl.metadata (3.0 kB)
Collecting SecretStorage>=3.2 (from keyring>=15.1->twine->autogen)
  Downloading SecretStorage-3.3.3-py3-none-any.whl.metadata (4.0 kB)
Collecting jeepney>=0.4.2 (from keyring>=15.1->twine->autogen)
  Downloading jeepney-0.8.0-py3-none-any.whl.metadata (1.3 kB)
Collecting nh3>=0.2.14 (from readme-renderer>=35.0->twine->autogen)
  Downloading nh3-0.2.17-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (1.7 kB)
Collecting docutils>=0.13.1 (from readme-renderer>=35.0->twine->autogen)
  Downloading docutils-0.20.1-py3-none-any.whl.metadata (2.8 kB)
Requirement already satisfied: Pygments>=2.5.1 in /home/codespace/.local/lib/python3.10/site-packages (from readme-renderer>=35.0->twine->autogen) (2.17.2)
Requirement already satisfied: charset-normalizer<4,>=2 in /home/codespace/.local/lib/python3.10/site-packages (from requests>=2.20->twine->autogen) (3.3.2)
Requirement already satisfied: idna<4,>=2.5 in /home/codespace/.local/lib/python3.10/site-packages (from requests>=2.20->twine->autogen) (3.6)
Requirement already satisfied: certifi>=2017.4.17 in /home/codespace/.local/lib/python3.10/site-packages (from requests>=2.20->twine->autogen) (2024.2.2)
Collecting markdown-it-py>=2.2.0 (from rich>=12.0.0->twine->autogen)
  Downloading markdown_it_py-3.0.0-py3-none-any.whl.metadata (6.9 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=12.0.0->twine->autogen)
  Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Collecting cryptography>=2.0 (from SecretStorage>=3.2->keyring>=15.1->twine->autogen)
  Using cached cryptography-42.0.5-cp39-abi3-manylinux_2_28_x86_64.whl.metadata (5.3 kB)
Collecting more-itertools (from jaraco.classes->keyring>=15.1->twine->autogen)
  Downloading more_itertools-10.2.0-py3-none-any.whl.metadata (34 kB)
Requirement already satisfied: cffi>=1.12 in /home/codespace/.local/lib/python3.10/site-packages (from cryptography>=2.0->SecretStorage>=3.2->keyring>=15.1->twine->autogen) (1.16.0)
Requirement already satisfied: pycparser in /home/codespace/.local/lib/python3.10/site-packages (from cffi>=1.12->cryptography>=2.0->SecretStorage>=3.2->keyring>=15.1->twine->autogen) (2.21)
Downloading autogen-1.0.16-py3-none-any.whl (30 kB)
Downloading autopep8-2.1.0-py2.py3-none-any.whl (44 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45.0/45.0 kB 1.1 MB/s eta 0:00:00
Downloading twine-5.0.0-py3-none-any.whl (37 kB)
Downloading importlib_metadata-7.1.0-py3-none-any.whl (24 kB)
Downloading keyring-25.0.0-py3-none-any.whl (37 kB)
Downloading pkginfo-1.10.0-py3-none-any.whl (30 kB)
Downloading pycodestyle-2.11.1-py2.py3-none-any.whl (31 kB)
Downloading readme_renderer-43.0-py3-none-any.whl (13 kB)
Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 54.5/54.5 kB 1.4 MB/s eta 0:00:00
Downloading rfc3986-2.0.0-py2.py3-none-any.whl (31 kB)
Downloading rich-13.7.1-py3-none-any.whl (240 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 240.7/240.7 kB 6.0 MB/s eta 0:00:00
Downloading docutils-0.20.1-py3-none-any.whl (572 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 572.7/572.7 kB 13.4 MB/s eta 0:00:00
Downloading jeepney-0.8.0-py3-none-any.whl (48 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 48.4/48.4 kB 1.2 MB/s eta 0:00:00
Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 87.5/87.5 kB 2.5 MB/s eta 0:00:00
Downloading nh3-0.2.17-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (777 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 777.1/777.1 kB 17.5 MB/s eta 0:00:00
Downloading SecretStorage-3.3.3-py3-none-any.whl (15 kB)
Downloading zipp-3.18.1-py3-none-any.whl (8.2 kB)
Downloading jaraco.classes-3.3.1-py3-none-any.whl (6.8 kB)
Downloading jaraco.context-4.3.0-py3-none-any.whl (5.3 kB)
Downloading jaraco.functools-4.0.0-py3-none-any.whl (9.8 kB)
Using cached cryptography-42.0.5-cp39-abi3-manylinux_2_28_x86_64.whl (4.6 MB)
Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Downloading more_itertools-10.2.0-py3-none-any.whl (57 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 57.0/57.0 kB 1.2 MB/s eta 0:00:00
Building wheels for collected packages: docopt
  Building wheel for docopt (pyproject.toml) ... done
  Created wheel for docopt: filename=docopt-0.6.2-py2.py3-none-any.whl size=13706 sha256=6d9ed686961dba8eac624d7e73c6105dc8c0c5ac57d34bea0119f6eb279e2c9b
  Stored in directory: /home/codespace/.cache/pip/wheels/fc/ab/d4/5da2067ac95b36618c629a5f93f809425700506f72c9732fac
Successfully built docopt
Installing collected packages: nh3, docopt, zipp, rfc3986, pycodestyle, pkginfo, more-itertools, mdurl, jeepney, jaraco.context, docutils, requests-toolbelt, readme-renderer, markdown-it-py, jaraco.functools, jaraco.classes, importlib-metadata, cryptography, autopep8, SecretStorage, rich, keyring, twine, autogen
Successfully installed SecretStorage-3.3.3 autogen-1.0.16 autopep8-2.1.0 cryptography-42.0.5 docopt-0.6.2 docutils-0.20.1 importlib-metadata-7.1.0 jaraco.classes-3.3.1 jaraco.context-4.3.0 jaraco.functools-4.0.0 jeepney-0.8.0 keyring-25.0.0 markdown-it-py-3.0.0 mdurl-0.1.2 more-itertools-10.2.0 nh3-0.2.17 pkginfo-1.10.0 pycodestyle-2.11.1 readme-renderer-43.0 requests-toolbelt-1.0.0 rfc3986-2.0.0 rich-13.7.1 twine-5.0.0 zipp-3.18.1
@milsteam4144 ➜ /workspaces/CTI-110 (main) $
@milsteam4144 ➜ /workspaces/CTI-110 (main) $ autogenstudio ui
bash: autogenstudio: command not found
@milsteam4144 ➜ /workspaces/CTI-110 (main) $ pip install pyautogen
Collecting pyautogen
  Downloading pyautogen-0.2.21-py3-none-any.whl.metadata (19 kB)
Collecting diskcache (from pyautogen)
  Downloading diskcache-5.6.3-py3-none-any.whl.metadata (20 kB)
Collecting docker (from pyautogen)
  Downloading docker-7.0.0-py3-none-any.whl.metadata (3.5 kB)
Collecting flaml (from pyautogen)
  Downloading FLAML-2.1.2-py3-none-any.whl.metadata (15 kB)
Requirement already satisfied: numpy<2,>=1.17.0 in /home/codespace/.local/lib/python3.10/site-packages (from pyautogen) (1.26.4)
Collecting openai>=1.3 (from pyautogen)
  Downloading openai-1.14.3-py3-none-any.whl.metadata (20 kB)
Collecting pydantic!=2.6.0,<3,>=1.10 (from pyautogen)
  Downloading pydantic-2.6.4-py3-none-any.whl.metadata (85 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 85.1/85.1 kB 2.7 MB/s eta 0:00:00
Collecting python-dotenv (from pyautogen)
  Downloading python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)
Collecting termcolor (from pyautogen)
  Downloading termcolor-2.4.0-py3-none-any.whl.metadata (6.1 kB)
Collecting tiktoken (from pyautogen)
  Downloading tiktoken-0.6.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)
Requirement already satisfied: anyio<5,>=3.5.0 in /home/codespace/.local/lib/python3.10/site-packages (from openai>=1.3->pyautogen) (4.3.0)
Collecting distro<2,>=1.7.0 (from openai>=1.3->pyautogen)
  Downloading distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
Requirement already satisfied: httpx<1,>=0.23.0 in /home/codespace/.local/lib/python3.10/site-packages (from openai>=1.3->pyautogen) (0.27.0)
Requirement already satisfied: sniffio in /home/codespace/.local/lib/python3.10/site-packages (from openai>=1.3->pyautogen) (1.3.1)
Collecting tqdm>4 (from openai>=1.3->pyautogen)
  Downloading tqdm-4.66.2-py3-none-any.whl.metadata (57 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 57.6/57.6 kB 1.7 MB/s eta 0:00:00
Requirement already satisfied: typing-extensions<5,>=4.7 in /home/codespace/.local/lib/python3.10/site-packages (from openai>=1.3->pyautogen) (4.10.0)
Collecting annotated-types>=0.4.0 (from pydantic!=2.6.0,<3,>=1.10->pyautogen)
  Downloading annotated_types-0.6.0-py3-none-any.whl.metadata (12 kB)
Collecting pydantic-core==2.16.3 (from pydantic!=2.6.0,<3,>=1.10->pyautogen)
  Downloading pydantic_core-2.16.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.5 kB)
Requirement already satisfied: packaging>=14.0 in /home/codespace/.local/lib/python3.10/site-packages (from docker->pyautogen) (24.0)
Requirement already satisfied: requests>=2.26.0 in /home/codespace/.local/lib/python3.10/site-packages (from docker->pyautogen) (2.31.0)
Requirement already satisfied: urllib3>=1.26.0 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from docker->pyautogen) (2.0.7)
Collecting regex>=2022.1.18 (from tiktoken->pyautogen)
  Downloading regex-2023.12.25-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (40 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40.9/40.9 kB 1.1 MB/s eta 0:00:00
Requirement already satisfied: idna>=2.8 in /home/codespace/.local/lib/python3.10/site-packages (from anyio<5,>=3.5.0->openai>=1.3->pyautogen) (3.6)
Requirement already satisfied: exceptiongroup>=1.0.2 in /home/codespace/.local/lib/python3.10/site-packages (from anyio<5,>=3.5.0->openai>=1.3->pyautogen) (1.2.0)
Requirement already satisfied: certifi in /home/codespace/.local/lib/python3.10/site-packages (from httpx<1,>=0.23.0->openai>=1.3->pyautogen) (2024.2.2)
Requirement already satisfied: httpcore==1.* in /home/codespace/.local/lib/python3.10/site-packages (from httpx<1,>=0.23.0->openai>=1.3->pyautogen) (1.0.4)
Requirement already satisfied: h11<0.15,>=0.13 in /home/codespace/.local/lib/python3.10/site-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai>=1.3->pyautogen) (0.14.0)
Requirement already satisfied: charset-normalizer<4,>=2 in /home/codespace/.local/lib/python3.10/site-packages (from requests>=2.26.0->docker->pyautogen) (3.3.2)
Downloading pyautogen-0.2.21-py3-none-any.whl (236 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 236.6/236.6 kB 7.0 MB/s eta 0:00:00
Downloading openai-1.14.3-py3-none-any.whl (262 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 262.9/262.9 kB 7.0 MB/s eta 0:00:00
Downloading pydantic-2.6.4-py3-none-any.whl (394 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 394.9/394.9 kB 9.7 MB/s eta 0:00:00
Downloading pydantic_core-2.16.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 34.5 MB/s eta 0:00:00
Downloading diskcache-5.6.3-py3-none-any.whl (45 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45.5/45.5 kB 1.3 MB/s eta 0:00:00
Downloading docker-7.0.0-py3-none-any.whl (147 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 147.6/147.6 kB 4.6 MB/s eta 0:00:00
Downloading FLAML-2.1.2-py3-none-any.whl (296 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 296.7/296.7 kB 8.1 MB/s eta 0:00:00
Downloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)
Downloading termcolor-2.4.0-py3-none-any.whl (7.7 kB)
Downloading tiktoken-0.6.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 34.7 MB/s eta 0:00:00
Downloading annotated_types-0.6.0-py3-none-any.whl (12 kB)
Downloading distro-1.9.0-py3-none-any.whl (20 kB)
Downloading regex-2023.12.25-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (773 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 774.0/774.0 kB 19.1 MB/s eta 0:00:00
Downloading tqdm-4.66.2-py3-none-any.whl (78 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.3/78.3 kB 2.5 MB/s eta 0:00:00
Installing collected packages: tqdm, termcolor, regex, python-dotenv, pydantic-core, flaml, distro, diskcache, annotated-types, tiktoken, pydantic, docker, openai, pyautogen
Successfully installed annotated-types-0.6.0 diskcache-5.6.3 distro-1.9.0 docker-7.0.0 flaml-2.1.2 openai-1.14.3 pyautogen-0.2.21 pydantic-2.6.4 pydantic-core-2.16.3 python-dotenv-1.0.1 regex-2023.12.25 termcolor-2.4.0 tiktoken-0.6.0 tqdm-4.66.2
@milsteam4144 ➜ /workspaces/CTI-110 (main) $ autogenstudio ui
bash: autogenstudio: command not found
@milsteam4144 ➜ /workspaces/CTI-110 (main) $ autogenstudio ui
bash: autogenstudio: command not found
@milsteam4144 ➜ /workspaces/CTI-110 (main) $ pip install autogenstudio
Collecting autogenstudio
  Downloading autogenstudio-0.0.56-py3-none-any.whl.metadata (11 kB)
Requirement already satisfied: pydantic in /usr/local/python/3.10.13/lib/python3.10/site-packages (from autogenstudio) (2.6.4)
Collecting fastapi (from autogenstudio)
  Downloading fastapi-0.110.0-py3-none-any.whl.metadata (25 kB)
Collecting typer (from autogenstudio)
  Downloading typer-0.11.0-py3-none-any.whl.metadata (13 kB)
Collecting uvicorn (from autogenstudio)
  Downloading uvicorn-0.29.0-py3-none-any.whl.metadata (6.3 kB)
Collecting arxiv (from autogenstudio)
  Downloading arxiv-2.1.0-py3-none-any.whl.metadata (6.1 kB)
Requirement already satisfied: pyautogen>=0.2.0 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from autogenstudio) (0.2.21)
Requirement already satisfied: python-dotenv in /usr/local/python/3.10.13/lib/python3.10/site-packages (from autogenstudio) (1.0.1)
Collecting websockets (from autogenstudio)
  Downloading websockets-12.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)
Requirement already satisfied: numpy<2.0.0 in /home/codespace/.local/lib/python3.10/site-packages (from autogenstudio) (1.26.4)
Requirement already satisfied: diskcache in /usr/local/python/3.10.13/lib/python3.10/site-packages (from pyautogen>=0.2.0->autogenstudio) (5.6.3)
Requirement already satisfied: docker in /usr/local/python/3.10.13/lib/python3.10/site-packages (from pyautogen>=0.2.0->autogenstudio) (7.0.0)
Requirement already satisfied: flaml in /usr/local/python/3.10.13/lib/python3.10/site-packages (from pyautogen>=0.2.0->autogenstudio) (2.1.2)
Requirement already satisfied: openai>=1.3 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from pyautogen>=0.2.0->autogenstudio) (1.14.3)
Requirement already satisfied: termcolor in /usr/local/python/3.10.13/lib/python3.10/site-packages (from pyautogen>=0.2.0->autogenstudio) (2.4.0)
Requirement already satisfied: tiktoken in /usr/local/python/3.10.13/lib/python3.10/site-packages (from pyautogen>=0.2.0->autogenstudio) (0.6.0)
Requirement already satisfied: annotated-types>=0.4.0 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from pydantic->autogenstudio) (0.6.0)
Requirement already satisfied: pydantic-core==2.16.3 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from pydantic->autogenstudio) (2.16.3)
Requirement already satisfied: typing-extensions>=4.6.1 in /home/codespace/.local/lib/python3.10/site-packages (from pydantic->autogenstudio) (4.10.0)
Collecting feedparser==6.0.10 (from arxiv->autogenstudio)
  Downloading feedparser-6.0.10-py3-none-any.whl.metadata (2.3 kB)
Requirement already satisfied: requests==2.31.0 in /home/codespace/.local/lib/python3.10/site-packages (from arxiv->autogenstudio) (2.31.0)
Collecting sgmllib3k (from feedparser==6.0.10->arxiv->autogenstudio)
  Downloading sgmllib3k-1.0.0.tar.gz (5.8 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: charset-normalizer<4,>=2 in /home/codespace/.local/lib/python3.10/site-packages (from requests==2.31.0->arxiv->autogenstudio) (3.3.2)
Requirement already satisfied: idna<4,>=2.5 in /home/codespace/.local/lib/python3.10/site-packages (from requests==2.31.0->arxiv->autogenstudio) (3.6)
Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from requests==2.31.0->arxiv->autogenstudio) (2.0.7)
Requirement already satisfied: certifi>=2017.4.17 in /home/codespace/.local/lib/python3.10/site-packages (from requests==2.31.0->arxiv->autogenstudio) (2024.2.2)
Collecting starlette<0.37.0,>=0.36.3 (from fastapi->autogenstudio)
  Downloading starlette-0.36.3-py3-none-any.whl.metadata (5.9 kB)
Collecting click>=8.0.0 (from typer->autogenstudio)
  Downloading click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
Requirement already satisfied: h11>=0.8 in /home/codespace/.local/lib/python3.10/site-packages (from uvicorn->autogenstudio) (0.14.0)
Requirement already satisfied: anyio<5,>=3.5.0 in /home/codespace/.local/lib/python3.10/site-packages (from openai>=1.3->pyautogen>=0.2.0->autogenstudio) (4.3.0)
Requirement already satisfied: distro<2,>=1.7.0 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from openai>=1.3->pyautogen>=0.2.0->autogenstudio) (1.9.0)
Requirement already satisfied: httpx<1,>=0.23.0 in /home/codespace/.local/lib/python3.10/site-packages (from openai>=1.3->pyautogen>=0.2.0->autogenstudio) (0.27.0)
Requirement already satisfied: sniffio in /home/codespace/.local/lib/python3.10/site-packages (from openai>=1.3->pyautogen>=0.2.0->autogenstudio) (1.3.1)
Requirement already satisfied: tqdm>4 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from openai>=1.3->pyautogen>=0.2.0->autogenstudio) (4.66.2)
Requirement already satisfied: packaging>=14.0 in /home/codespace/.local/lib/python3.10/site-packages (from docker->pyautogen>=0.2.0->autogenstudio) (24.0)
Requirement already satisfied: regex>=2022.1.18 in /usr/local/python/3.10.13/lib/python3.10/site-packages (from tiktoken->pyautogen>=0.2.0->autogenstudio) (2023.12.25)
Requirement already satisfied: exceptiongroup>=1.0.2 in /home/codespace/.local/lib/python3.10/site-packages (from anyio<5,>=3.5.0->openai>=1.3->pyautogen>=0.2.0->autogenstudio) (1.2.0)
Requirement already satisfied: httpcore==1.* in /home/codespace/.local/lib/python3.10/site-packages (from httpx<1,>=0.23.0->openai>=1.3->pyautogen>=0.2.0->autogenstudio) (1.0.4)
Downloading autogenstudio-0.0.56-py3-none-any.whl (2.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.7/2.7 MB 35.2 MB/s eta 0:00:00
Downloading arxiv-2.1.0-py3-none-any.whl (11 kB)
Downloading feedparser-6.0.10-py3-none-any.whl (81 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 81.1/81.1 kB 2.5 MB/s eta 0:00:00
Downloading fastapi-0.110.0-py3-none-any.whl (92 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 92.1/92.1 kB 2.9 MB/s eta 0:00:00
Downloading typer-0.11.0-py3-none-any.whl (43 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.6/43.6 kB 1.3 MB/s eta 0:00:00
Downloading uvicorn-0.29.0-py3-none-any.whl (60 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.8/60.8 kB 1.8 MB/s eta 0:00:00
Downloading websockets-12.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (130 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 130.2/130.2 kB 3.7 MB/s eta 0:00:00
Downloading click-8.1.7-py3-none-any.whl (97 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.9/97.9 kB 3.1 MB/s eta 0:00:00
Downloading starlette-0.36.3-py3-none-any.whl (71 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 71.5/71.5 kB 2.2 MB/s eta 0:00:00
Building wheels for collected packages: sgmllib3k
  Building wheel for sgmllib3k (pyproject.toml) ... done
  Created wheel for sgmllib3k: filename=sgmllib3k-1.0.0-py3-none-any.whl size=6049 sha256=b73b1a514815ed274a16c38a3b393873a4c3039ebaef26e5605b0035c5df4f83
  Stored in directory: /home/codespace/.cache/pip/wheels/f0/69/93/a47e9d621be168e9e33c7ce60524393c0b92ae83cf6c6e89c5
Successfully built sgmllib3k
Installing collected packages: sgmllib3k, websockets, feedparser, click, uvicorn, typer, starlette, arxiv, fastapi, autogenstudio
Successfully installed arxiv-2.1.0 autogenstudio-0.0.56 click-8.1.7 fastapi-0.110.0 feedparser-6.0.10 sgmllib3k-1.0.0 starlette-0.36.3 typer-0.11.0 uvicorn-0.29.0 websockets-12.0
@milsteam4144 ➜ /workspaces/CTI-110 (main) $ autogenstudio ui
 
Initialized application data folder: /home/codespace/.autogenstudio
INFO:     Started server process [6813]
INFO:     Waiting for application startup.
***** App started *****
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8081 (Press CTRL+C to quit)