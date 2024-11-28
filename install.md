# Installation of LLM_P

> ***Note**: The installation process of this project is relatively simple.*

- Create LLM_P env
```
conda create -n LLM_P python=3.10
conda activate LLM_P
```

- Install FastDownward 

```
cd Task_Planning/LLM_P
./build.py
```

If necessary, see FastDownward's [documentation](https://drive.google.com/file/d/16HlP14IN06asIXYAZ8RHR1P7-cEYwhA6/view) for more detailed installation instructions.

- Install neccessary packages

```
pip install openai==0.28.1 backoff==2.2.1
```