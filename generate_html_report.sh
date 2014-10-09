if [ $1 ]; then
  input="./reports/WR$1.md"
  output="itlab-vision-WR$1.html"
else
  input="./reports/WR`date +%V`.md"
  output="itlab-vision-WR`date +%V`.html"
fi

if [ ! -f $output ] || [ $input -nt $output ]; then
  echo "Source file was updated!"
  echo "File $input will be converted to $output"
  pandoc --self-contained $input -o $output
  echo "Done"
else
  echo "Nothing to update, waiting..."
fi
