# A counter for the number of successful runs

# Loop indefinitely until a difference is found
while true; do
    # Increment and print the current test number
    i=$((i+1))
    echo "Running test #$i..."

    # 1. Generate the test input
    python3 test.py > /tmp/idfk.in

    # 2. Run the first program
    python3 sol.py /tmp/idfk.in > /tmp/p1.out

    # 3. Run the second program
    cat /tmp/idfk.in | java /tmp/Factovisors.java > /tmp/p2.out

    # 4. Check for differences quietly (-q flag)
    # If diff finds a difference, its exit code will be non-zero,
    # causing the 'if' condition to be true.
    if ! diff -q /tmp/p1.out /tmp/p2.out > /dev/null; then
        echo "✅ Difference found after $i runs!"
        break # Exit the loop
    fi
done

# Once the loop is broken, show the input that caused the failure and the full diff
echo "---"
echo "🕵️ Failing Input (/tmp/idfk.in):"
cat /tmp/idfk.in
echo "---"
echo "🔍 Full Diff:"
diff /tmp/p1.out /tmp/p2.out
