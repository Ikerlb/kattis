python test.py > /tmp/test.txt
diff <(cat /tmp/test.txt | python sol.py) <(cat /tmp/test.txt | cargo script sol.rs)
