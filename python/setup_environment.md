# Python Environment Setup Guide

Before starting to build more complex Python applications (especially in AI and Data Science), it is considered a best practice to use **Virtual Environments**.

A virtual environment is an isolated space on your computer where you can install packages (like Pandas, NumPy, or Scikit-Learn) specifically for one project, without affecting the rest of your system or other projects.

Here is a step-by-step guide to setting up your Python virtual environment.

---

## Step 1: Verify Python is Installed

First, ensure you have Python 3 installed on your machine. Open your terminal (Mac/Linux) or Command Prompt/PowerShell (Windows) and type:

```bash
python3 --version
# OR
python --version
```
*If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).*

## Step 2: Navigate to your Project Directory

Use the `cd` (change directory) command to navigate to the folder where you want to work. For example:

```bash
cd /path/to/your/ai-learning/python
```

## Step 3: Create the Virtual Environment

Python comes with a built-in module called `venv` to create virtual environments. Run the following command. This will create a new hidden folder called `.venv` in your current directory, which will hold your isolated Python setup.

```bash
python3 -m venv .venv
# On some Windows setups, you might just use: python -m venv .venv
```
*(Note: You can name the environment folder anything, but `.venv` or `venv` are standard conventions).*

## Step 4: Activate the Virtual Environment

You must **activate** the environment every time you open a new terminal to work on this project.

### On macOS and Linux:
```bash
source .venv/bin/activate
```

### On Windows (Command Prompt):
```cmd
.venv\Scripts\activate.bat
```

### On Windows (PowerShell):
```powershell
.venv\Scripts\Activate.ps1
```

**How do you know it worked?**
You should see `(.venv)` appear at the very beginning of your terminal prompt. For example: `(.venv) user@macbook python % `

## Step 5: Install Packages (Optional)

Once activated, any packages you install will be contained within this environment. For AI and Data Science, you typically use `pip`.

```bash
# Example: Installing popular data science libraries
pip install pandas numpy matplotlib
```

## Step 6: Deactivate (When you're done)

When you are finished working on your project and want to return to your normal system terminal, simply type:

```bash
deactivate
```
The `(.venv)` prefix will disappear from your terminal prompt.
