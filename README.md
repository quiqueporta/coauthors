# coauthors
Add coauthors to your last git commit message.

## Install

To install **coauthors**, just run:

```sh
$ sudo python3 -m pip install coauthors # for protected env --break-system-packages
```

## Configure

First create a config file with your coauthors.

Example ~/.coauthors.json:

```javascript
{
  "Faemino":
  {
    "name": "Juan Carlos Arroyo",
    "email": "faemino@comedian.com"
  },
  "Cansado":
  {
    "name": "Angel Javier Pozuelo",
    "email": "cansado@comedian.com"
  }
}
```

Then add the following line to your sources file (.bashrc, .zshrc, ...):

```sh
export PATH="$HOME/.local/bin:$PATH"
export COAUTHORS_FILE="/home/<user>/.coauthors.json"
```

## Usage

You can coauthor your commit with one friend
```sh
$ coauthors Faemino
```

or with many
```sh
$ coauthors Faemino Cansado
```

You can list your available coauthors
```sh
$ coauthors --list
```
