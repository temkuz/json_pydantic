# Json_Pydantic


Json_Pydantic is a utility for converting json files to Pydantic models

## Install

```commandline
pip install .
```

## Usage

You can use this tool with two ways

- As module
  - Windows
      ```commandline
      py -m json_pydantic -i INPUT_FILE -o OUTPUT_FILE 
      ```
  - Linux
    ```commandline
    python3 -m json_pydantic -i INPUT_FILE -o OUTPUT_FILE
    ```
- As cli tool
  ```commandline
  json_pydantic -i INPUT_FILE -o OUTPUT_FILE
  ```

## More info

You can get more info about settings with command

```commandline
json_pydantic -h
```