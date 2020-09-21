# Shhhhhh...
Congratulations, you are so close to the secret flag:
```
nsa{1������������������������c0�pl3�3�}
```
## FAQ
### Is the flag corrupted?
Well, due to frequent electromagnetic radiation, parts of the flag got corrupted. The corrupted characters are marked with replacement characters: `�`. We confirmed that the rest of the characters are fine.
### Is there a way to recover the flag from this?
We tried lots of data recovery apps, but we are not sure if they are reliable. (each app outputs a different flag) Luckily we had already developed an offline flag integrity checker available in this repository: [`check-flag.py`](./check-flag.py). Running the script tells you whether your flag is correct or not.
### What's `prog.out` for?
In order to make it more difficult for hackers to understand the inner workings of the flag checker and possibly extract the flag, we obfuscated the script. It interprets magic codes from `prog.out`, which means that this binary file must be in the same working directory as `check-flag.py` when you run the script.
