for f in *.ui
  do pyuic5 $f -o ${f%%.*}_GEN.py
done
