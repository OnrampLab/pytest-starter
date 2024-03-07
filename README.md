# pytest-starter

## Set up project

## Install package manager - poetry

```bash
docker-compose build
```

## Install packages

### Copy config

```
cp config.yml.example config.yml
cp .env.example .env
```

## Running tests

```
python -m pytest tests/test_registration.py
```

```
python -m pytest tests/
```

```
python -m pytest -s tests/test_contact_report.py
```

To generate xml results, run the following command : `pytest Tests --junitxml="result.xml"`

For more on Pytest, go [here.](https://docs.pytest.org/en/stable/)

## Clear cache

Windows

```
Remove-Item -Recurse -Force .pytest_cache
```

## CI/CD

### Encrypt config.yml to AWS S3 for staging or production

Prerequisites:

1. You need to create a KMS key in AWS.

2. Update aws setting in `pytest.ini`

3. You can create `config.yml.dev`, `config.yml.staging` and `config.yml.production`. And then doing encryption before running CI/CD pipeline.

4. Do encryption

```bash
$ export KMS_KEY_ID="your_kms_key_id"
$ docker-compose run app python tools/scripts/encrypt_config.py [Environment]
```

Environment will be:
  - `dev`: for feature branch
  - `staging` for master branch
  - `production` for tag

It will create a S3 file object under `pytest/encrypted_config.yml` of S3 bucket.

Production uses `starter` bucket. Staging uses `starter-staging` bucket.

## Contribution

```
git checkout YOUR_BRANCH
git add .
git commit -m "YOUR_MESSAGE"
git push origin YOUR_BRANCH
```
