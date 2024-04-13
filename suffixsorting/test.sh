while [ $? -eq 0 ]
do
    echo "not yet"
    python test.py > /tmp/test.txt
    cat /tmp/test.txt | cargo script sol.rs > /dev/null
done
