# Cross-platform Makefile for executing Jupyter notebooks in a Python venv

PY=python
VENV=.venv
OUTPUT=outputs

# Detect Windows vs Unix
ifeq ($(OS),Windows_NT)
    PYBIN=$(VENV)/Scripts/python.exe
    JUPYTER=$(VENV)/Scripts/jupyter.exe
    MKDIR=if not exist $(OUTPUT) mkdir $(OUTPUT)
    RM=rd /s /q $(VENV) & rd /s /q $(OUTPUT)
else
    PYBIN=$(VENV)/bin/python
    JUPYTER=$(VENV)/bin/jupyter
    MKDIR=mkdir -p $(OUTPUT)
    RM=rm -rf $(VENV) $(OUTPUT)
endif

.PHONY: setup install kernel run-all preprocess train evaluate visualize clean

# 1. Create virtual environment & install base tools
setup:
	$(PY) -m venv $(VENV)
	$(PYBIN) -m pip install --upgrade pip setuptools wheel
	$(PYBIN) -m pip install jupyter nbconvert jupyter_client ipykernel
	$(PYBIN) -m ipykernel install --user --name=project-kernel
	make install

# 2. Install project dependencies
install:
	$(PYBIN) -m pip install -r requirements.txt

# 3. Run entire pipeline
run-all: preprocess train evaluate

# 4. Execute preprocessing notebooks
preprocess:
	$(MKDIR)
	$(JUPYTER) nbconvert --to notebook --execute notebooks/01_EDA.ipynb --output 01_EDA_out.ipynb --output-dir $(OUTPUT)
	$(JUPYTER) nbconvert --to notebook --execute notebooks/02_Data_cleaning.ipynb --output 02_Data_cleaning_out.ipynb --output-dir $(OUTPUT)

# 5. Execute feature engineering + model training
train:
	$(JUPYTER) nbconvert --to notebook --execute notebooks/03_Feature_eng.ipynb --output 03_Feature_eng_out.ipynb --output-dir $(OUTPUT)
	$(JUPYTER) nbconvert --to notebook --execute notebooks/04_model.ipynb --output 04_model_out.ipynb --output-dir $(OUTPUT)

# 6. Execute evaluation notebook
evaluate:
	$(JUPYTER) nbconvert --to notebook --execute notebooks/05_Test_evaluation.ipynb --output 05_Test_evaluation_out.ipynb --output-dir $(OUTPUT)

# 7. Optional visualization
# visualize:
# 	$(JUPYTER) nbconvert --to notebook --execute notebooks/visualize.ipynb --output notebooks/$(OUTPUT)/visualize_out.ipynb

# 8. Remove virtual environment + output files
clean:
	$(RM)
