# crypto-arsenal-code-test
The source code for the position of intern backend engineering test in crypto-arsenal

# Run the code
use the following command to fetch the code
```shell
git clone https://github.com/chc-tw/crypto-arsenal-code-test.git
cd crypto-arsenal-code-test
```
## Docker image
```bash
docker pull chc90419/crypto_arsenal_test:latest
docker run --rm chc90419/crypto_arsenal_test:latest python main.py
```
## environment settings
```bash
conda env create -f environment.yml
conda activate code_test
python main.py
```