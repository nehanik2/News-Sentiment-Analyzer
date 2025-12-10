PY=python
VENV=.venv
PYBIN=$(VENV)/Scripts/python.exe

.PHONY: setup install build test run-all clean preprocess train evaluate visualize

setup:
	$(PY) -m venv $(VENV)
	$(PYBIN) -m pip install --upgrade pip setuptools wheel nbconvert
	make install

install:
	$(PYBIN) -m pip install -r requirements.txt

build:
	@echo "No compiled components—skipping build step."

run-all: preprocess train evaluate # visualize

preprocess:
	$(PYBIN) -m nbconvert --to notebook --execute notebooks/01_EDA.ipynb --output 01_EDA_out.ipynb
	$(PYBIN) -m nbconvert --to notebook --execute notebooks/02_Data_cleaning.ipynb --output 02_Data_cleaning_out.ipynb

train:
	$(PYBIN) -m nbconvert --to notebook --execute notebooks/03_Feature_eng.ipynb --output 03_Feature_eng_out.ipynb
	$(PYBIN) -m nbconvert --to notebook --execute notebooks/04_model.ipynb --output 04_model_out.ipynb

evaluate:
	$(PYBIN) -m nbconvert --to notebook --execute notebooks/05_Test_evaluation.ipynb --output 05_Test_evaluation_out.ipynb

visualize:
	$(PYBIN) -m nbconvert --to notebook --execute notebooks/visualize.ipynb --output visualize_out.ipynb

# test:
# 	$(PYBIN) -m nbconvert --to notebook --execute notebooks/visualize.ipynb --output visualize_out.ipynb

# clean:
# 	rm -rf $(VENV) outputs models figs
