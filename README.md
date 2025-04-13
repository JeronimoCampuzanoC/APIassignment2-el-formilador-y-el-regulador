# 📌 Project README
```
██████╗ ██████╗  █████╗  
██╔══██╗██╔══██╗██╔══██╗ 
██████╔╝██║  ██║███████║ 
██╔═══╝ ██║  ██║██╔══██║ 
██║     ██████╔╝██║  ██║ 
╚═╝     ╚═════╝ ╚═╝  ╚═╝
----------------------------
 ██████╗███████╗ ██████╗ 
██╔════╝██╔════╝██╔════╝ 
██║     █████╗  ██║  ███╗
██║     ██╔══╝  ██║   ██║
╚██████╗██║     ╚██████╔╝
 ╚═════╝╚═╝      ╚═════╝ 
 ----------------------------
           _____ _____ 
     /\   |  __ \_   _|
    /  \  | |__! || |  
   / /\ \ |  ___/ | |  
  / ____ \| |    _| |_ 
 /_/    \_\_|   |_____|
                       
                       

```
# 🧾 Table of Contents

1. [📖 Description](#-description)
2. [📚 Class Information](#-class-information)
3. [👨‍🏫 Teacher](#-teacher)
4. [👨‍🎓 Students](#-students)
5. [💻 System Information](#-system-information)
6. [🚀 Running](#-running)
    - [Compilation](#compilation)
    - [Execution](#execution)
7. [📖 Explanation](#-explanation)
    - [Algorithm 1](#algorithm-1)
    - [Algorithm 2](#algorithm-2)
    - [Algorithm 3](#algorithm-3)

## 📖 Description
This project focuses on implementing and analyzing a Context-Free Grammar (CFG) and a Pushdown Automaton (PDA) for language recognition. It consists of implementation of three main algorithms in the following order:

+ String Generation according to the grammar G       𝑺 → 𝒂𝑺𝒃 | e
+ PDA that recognizes strings from the CFG.
+ Leftmost derivation tree for sentential form and configuration of the PDA.

And connect all of this through an API that will be queried by a web page to display the results.

## 📚 Class Information
- **Class Number:** 7308  

## 👨‍🏫 Teacher
- **Adolfo Andrés Castro Sánchez** 

## 👨‍🎓 Students
- **Jeronimo Campuzano Castaño** 
- **Andres Perez Quinchia**  

## 💻 System Information
- **OS:** Ubuntu 24.04.2 LTS x86_64  
- **Programming Language:** Python
- **Interpreter Version:** Python 3.12.3

---

## 🚀 Running 


## 📖 Explanation
first we traduce the c++ algorithms to python

Create the virtual enviroment and we install the following dependencies with the requirements file

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

After that we activate the web server

```bash
python3 -m uvicorn main:app --reload
```

And use streamlit to try the algorithms

```bash
streamlit run app.py
```


