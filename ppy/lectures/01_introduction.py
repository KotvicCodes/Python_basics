# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# # Welcome to PPY1 lecture #1
#
# 1. Grab a place, start your computer, if you can
# 2. Have a look at an intro survey [bit.ly/ppy1](http://bit.ly/ppy1), which will help us organize the course a bit better
# 3. Bookmark the repository: [gitlab.fjfi.cvut.cz/ksi/ppy1-2026](https://gitlab.fjfi.cvut.cz/ksi/ppy1-2026), open the `01_introduction.ipynb`, where you will find everything for today

# %% [markdown] slideshow={"slide_type": "slide"}
# # Let us introduce the lecturers...
#
# This year the course has two lecturers:

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Jakub Klinkovský
#
# My name is Jakub Klinkovský, and I will be your lecturer. I also:
#
# * Teach other courses at the Department of Software Engineering, FNSPE CTU in Prague: ZPRO, PROP, INTA, CLOUD, and more
# * Do research in [Computational Fluid Dynamics](https://en.wikipedia.org/wiki/Computational_fluid_dynamics)
# * Love programming in Python and C++ and CUDA
#
# **Disclaimer:** I certainly do *not* know everything, even ChatGPT knows Python more than me! But it will also tell you a lot of nonsense, whereas I will not 😉

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Matej Mojzeš
#
# My name is Matej Mojzeš, and I will be your lecturer. I also:
#
# * Have a Ph.D. in integer optimization heuristics from the Department of Software Engineering, FNSPE CTU in Prague  
# * Lead data scientists and data engineers at [SharpGrid](https://www.sharpgrid.com) (using Python, of course!)  
# * Have years of experience in Business Intelligence, Data Warehousing, Engineering, and Data Science in both startup and corporate environments  
#
# **Disclaimer:** I am a big fan of Python and have been actively using it for many years. I certainly do *not* know everything about it, but I love learning—and I hope we can learn something new together! 🙂

# %% [markdown] slideshow={"slide_type": "slide"}
# # Why two lecturers?
#
# The course will have 2 parallel classes:
#
# 1. 18PPY1 – Czech group (*big*) – Jakub Klinkovský
# 2. 18YPPY1 – English group (*small*) – Matej Mojzeš
#
# Who would like to switch the group, now is the right time to ask for it.

# %% [markdown] slideshow={"slide_type": "slide"}
# # So, why bother learning more about Python?

# %% [markdown] slideshow={"slide_type": "fragment"}
# ![image](figures/python_et_al.png)
#
# Because of the ease of use, versatility, and large community which made it a popular choice for developers of all skill levels. From my point of view, currently, it is still the sweet spot between prototyping and production-grade programming language.
#
# Source of the data: [trends.google.com](https://trends.google.com/trends/explore?date=all&q=%2Fm%2F05z1_,%2Fm%2F07sbkfb,%2Fm%2F0jgqg,%2Fm%2F053_x)

# %% [markdown] slideshow={"slide_type": "slide"}
# # PPY1 outline
#
# 1. Introduction and workspace setup (Jupyter and/or VSCode)
# 2. Object-oriented programming and functional programming in Python
# 3. Type hints and type checking
# 4. Introduction to NumPy and SciPy libraries
# 5. Data analysis and processing using the pandas library
# 6. Code testing, introduction to the PyTest and Hypothesis libraries

# %% [markdown] slideshow={"slide_type": "subslide"}
# 7. Data visualization using the matplotlib and seaborn libraries
# 8. Creating web applications using the Streamlit framework
# 9. Data export, working with data formats such as JSON, XML, CSV, and Parquet
# 10. Working with SQL databases
# 11. Scraping data from the internet
# 12. Distributed computing using PySpark
# 13. Creating documentation and command-line interfaces

# %% [markdown] slideshow={"slide_type": "fragment"}
# **If you feel you know all of this already, feel free to deliver your project ASAP and skip the rest of the lectures**!

# %% [markdown] slideshow={"slide_type": "slide"}
# # To pass PPY1... 
#
# ...you need to deliver and defend your project:
#
# * It should prove that you have mastered most of the topics covered during the semester (specific requirements will be announced later)
# * I would like you to choose your own topic, but I can help with the selection, or provide some options.

# %% [markdown] slideshow={"slide_type": "fragment"}
# An example: a scientific project processing experimental data using pandas and numpy packages, delivered as Jupyter notebook.

# %% [markdown] slideshow={"slide_type": "fragment"}
# Another example: a game built using OOP, covered with PyTest unit tests, and documented using docstrings.

# %% [markdown] slideshow={"slide_type": "fragment"}
# Or... a CLI tool, that will read data stored in an SQL database, and visualize them in an interactive way using a Streamlit dashboard.

# %% [markdown] slideshow={"slide_type": "subslide"}
# ![image](figures/learning.jpeg)
#
# To get the most of this Python course, I strongly encourage you to present your work to your colleagues during the semester.

# %% [markdown] slideshow={"slide_type": "fragment"}
# ...which brings us to the question of...

# %% [markdown] slideshow={"slide_type": "subslide"}
# # What are the deadlines?
#
# * Deadline for selecting a topic: **April 1, 2026** (topics selected later will not be approved)
# * Deadline for submitting a *first version* of your project: **July 31, 2026**
# * Deadline for defending the *final version* of your project: **September 18, 2026** (this is the end of the academic year, so you need to submit your final version before this date)
#
# You will have the opportunity to present your project to the class at the end of the lectures in the second half of the semester.
# This way, you can get feedback from your friends and improve your presentation skills.
#
# Alternatively, you can defend your project privately during the examination period.

# %% [markdown] slideshow={"slide_type": "slide"}
# # And finally... something about Python 😉
#
# Materials for the course are available on GitLab FJFI: https://gitlab.fjfi.cvut.cz/ksi/ppy1-2026
# First, we will learn how to synchronize the content of the repository on JupyterHub and your local computer.

# %% [markdown] slideshow={"slide_type": "fragment"}
# ## 1. JupyterHub FJFI
#
# Click on the blue "Synchronize to JupyterHub" button on the project page on GitLab.
#
# (JupyterHub is a convenient web-based environment for Python programming, which we used in ZPRO.
# It also has all packages needed for PPY1 installed, so you will not have to install anything.
# But for some lectures, you will need to use your own computer for programming.)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## 2. Synchronization on your own system
#
# First, we need to ensure that several tools are installed.
# Unfortunately, each tool can be installed in many different ways... 😅
#
# 1. **Git:** try to run `git` in a terminal, go to [Git official website](https://git-scm.com/install/) if it is not available
# 2. **Python:** try to run `python` or `python3` in a terminal. If it is not installed, you can install it:
#
#     - [Microsoft store](https://apps.microsoft.com/detail/9pnrbtzxmb4z?ocid=webpdpshare) (Windows), or [Homebrew](https://brew.sh/) (macOS), or [Linux package manager](https://docs.python.org/3/using/unix.html)
#     - manually from the [Python official website](https://www.python.org/downloads/)
#     - using the `uv` tool (see below)
#     
# 3. **uv:** a modern Python package and project manager
#
#     See [Installing uv](https://docs.astral.sh/uv/getting-started/installation/), pick a familiar installation method, and ensure that you can run `uv` in a terminal.
#     
#     If you need, you can [install Python using uv](https://docs.astral.sh/uv/guides/install-python/).
#     This is also useful for installing a specific version of Python which is not available on your system.

# %% [markdown] slideshow={"slide_type": "subslide"}
# When you have all the tools, download the [git-pull.py](./git-pull.py) script and run it with `uv`:
#
# ```txt
# cd C:\Users\yourname\Downloads
# uv run git-pull.py
# ```
#
# What happens:
#
# - `uv` checks *dependencies* of the script and installs the required packages in a separate *environment*
# - executes the script with Python in the appropriate environment
# - the script runs `git` to clone the repository from GitLab in a new location, or pull new commits from GitLab in an existing local repository
#
# **Hint:** Notice the project layout: [lectures](./lectures/) directory for prepared content, [exercises](./exercises/) for your own code.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Development environment
#
# After we have Python, the next essential thing for PPY1 is to have an *integrated development environment* (IDE):
#
# 1. FJFI Jupyter Hub on [jupyter.fjfi.cvut.cz](https://jupyter.fjfi.cvut.cz/), which you know from ZPRO
# 2. *Jupyter Lab* installed on your computer (same environment as on Jupyter Hub, but with your local files)
# 3. Full desktop application, such as [Visual Studio Code](https://code.visualstudio.com) (VSCode) or [PyCharm](https://www.jetbrains.com/pycharm/)
#
# For IDE, I recommend VSCode or VSCodium which was introduced in [ZPRO](https://gitlab.fjfi.cvut.cz/ksi/zpro-2025-public/-/blob/main/10%20VSCodium.ipynb), but feel free to use whatever suits your needs and preferences.
#
# **Note:** All popular IDEs are currently advertised as "AI-enhanced" or "AI code editor", but we will not be using any AI features in this course.

# %% [markdown] slideshow={"slide_type": "slide"}
# # VSCode workspace setup
#
# We have prepared a [VSCode profile](../PPY1.code-profile) which you can use to set up an environment equivalent to what you see on the screen.
# The profile includes:
#
# - common extensions
# - common settings
# - a few key bindings
#
# We should be ready for the *Hello World* exercise!
# Write a *Hello World* program in Python and make sure it can be run on your computer.
#
# **Hint:** Notice the project layout: [lectures](./lectures/) directory for prepared content, [exercises](./exercises/) for your own code.
# In any case, **make sure you backup your work**.

# %% [markdown] slideshow={"slide_type": "slide"}
# # About Python packages and environments
#
# One of the reasons behind Python's popularity is its vast collection of free and open-source libraries.
# These libraries are installed as **packages** – archives in a specific format that contain the code of the library.
#
# You can control the installation, uninstallation, and updating of packages using a **package manager** program.
# Unfortunately, the Python ecosystem has too many popular package managers (at least 10) 😅
# The most common package manager is *pip*:
#
# - Pip stands for "Preferred Installer Program" or recursively "Pip Installs Packages".
# - Pip is primarily used to install Python packages from the Python Package Index (PyPI) or other sources.
# - You can install a package by running the command `pip install <package_name>` (which you probably did already).

# %% [markdown]
# Pip also allows you to manage installed packages by providing commands to upgrade, uninstall, or list them. For example:
#
# ```
# pip install --upgrade <package_name>
# pip uninstall <package_name>
# pip list
# ```
#
# **Hint:** You can also manage packages using `uv` which contains a frontend for `pip`.
# You can simply prefix any `pip` command with `uv`, such as `uv pip install <package_name>`.
# See [The pip interface](https://docs.astral.sh/uv/pip/) in the documentation for details.

# %% [markdown]
# Furthermore, pip can be helpful in some more advanced scenarios, where you need to carefully control the environment your application runs in using a virtual environment, or `venv`, managing the dependencies using a "requirements" file, or, for example, distribute your own packages.
#
# We will not cover pip in more detail within PPY1, but you can find very helpful resources here: https://docs.python.org/3/tutorial/venv.html.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Jupyter Lab on your own computer
#
# To install Jupyter Lab, just run `pip/pip3 install jupyterlab` in your console. You can run it then using `jupyter lab` command. More information on [jupyter.org/install](https://jupyter.org/install).
#
# 1. Start your `jupyter lab` in the console (in case you have not done it already, of course)
# 2. In the UI (within web browser, which should start automatically), create a **New notebook** with Python kernel, type `print('Hello World')` in the first cell, execute it using the Run button and the result should look like this:
#
# ![image](figures/hello_world.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# So, what just happened?
#
# * You have executed one line of python code
# * Python (in a "kernel") is still running on your computer, ready to execute the code in that cell again, or any new cell you create and in the order in which you will run them
# * Results (visual outputs) of the cells will remain in the notebook after you shut down the Python kernel, you can get back to it anytime you want
#

# %% [markdown] slideshow={"slide_type": "fragment"}
# Just a couple of notes:
# * To maximize the chance you will get the same output when running the notebook again, you should "restart & run all cells" in your notebook before saving it (but sometimes this is computationally not possible, so you just need to think in advance, to eg. not overwrite memory, delete necessary cells, etc.)
# * You have witnessed how reproducible research can be easily implemented, see a [Nature article](http://www.nature.com/news/interactive-notebooks-sharing-the-code-1.16261) for more on this topic
# * For learning purposes, we will be primarily using this interactive coding approach (rather than programming larger scripts/modules and running them all in once)

# %% [markdown] slideshow={"slide_type": "subslide"}
# Let's have a look at the common tricks the Jupyter Lab can do, mainly:
#
# * Organize notebooks
# * Manage kernels
# * Work with notebooks (more at once, even the same notebooks)
# * Work with other file formats — python, markdown, data, text...

# %% [markdown] slideshow={"slide_type": "slide"}
# # Last, but not least
#

# %% slideshow={"slide_type": "fragment"}
magic = "As you can see, this slideshow can run Python code inside the slide. This is another power of Jupyter notebooks!"

# %% slideshow={"slide_type": "fragment"}
print(magic)

# %% [markdown] slideshow={"slide_type": "subslide"}
# **Inspiration/disclaimer**: Parts of this document have been created using [W3schools](https://www.w3schools.com), [Stack Overflow](https://stackoverflow.com), or [ChatGPT](https://chat.openai.com) (including a critical evaluation of the output). This is to demonstrate the power of publicly available resources. Make sure you will use them to your advantage too. Try to research what you want online, learn on your own and at your own pace, and feel free to ask me questions / discuss topics that interest you. 
#
# In general, I am very happy to share my knowledge, experience, or opinions with you, rather than just repeat what is easy to find online.
