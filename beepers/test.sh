python test.py > /tmp/test.in
diff <(cat /tmp/test.in | python sol2.py) <(cat /tmp/test.in | python sol.py)
