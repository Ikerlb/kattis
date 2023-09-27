python test.py > /tmp/test.in

time cat /tmp/test.in | ./a.out > /tmp/cpp.ans
time cat /tmp/test.in | cargo script sol.rs > /tmp/rust.ans
