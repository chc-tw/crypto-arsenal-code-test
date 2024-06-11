# crypto-arsenal-code-test
The source code for the test of intern backend engineering in crypto-arsenal

# Run the code
use the following command to fetch the code
```shell
git clone https://github.com/chc-tw/crypto-arsenal-code-test.git
cd crypto-arsenal-code-test
```
## Docker image
use the following command to run the Docker image and code
```bash
docker pull chc90419/crypto_arsenal_test:latest
docker run --rm chc90419/crypto_arsenal_test:latest python main.py
```
## Conda environment
use the following command to rebuld the conda environment and run the code
```bash
conda env create -f environment.yml
conda activate code_test
python main.py
```