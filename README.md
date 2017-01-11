# Learn Python the Hard Way

## Rename multiple files with git
```
for i in $(find . -iname "ex?.py"); do
    git mv "$i" "$(echo ${i/ex/ex0})";
done
```
