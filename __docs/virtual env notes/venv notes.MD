## main way to create a virtual environment using CLI

```sh
# Create a virtual environment named 'venv' in current directory
python -m venv myenv
```

# Remove the old environment
```sh
rm -rf myenv
```

## After creating, you need to activate it:
### Bash
```sh
source myenv/Scripts/activate
```

### PS
```powershell
.\myenv\Scripts\activate
# Get all running processes and sort by CPU usage
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
```

## for MacOS
```sh
source myenv/bin/activate
```

## To deactivate any virtual environment:
```sh
deactivate
```