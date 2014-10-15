if [ $1 ]; then
  input=$1
  echo "Will process $1"
else
  input="./`date +%Y-%m`/WW`date +%F`.md"
fi

output="itlab-vision-weekly-report-WW`date +%F`.html"

if [ ! -f $output ] || [ $input -nt $output ]; then
  echo "Source file was updated!"
  echo "File $input will be converted to $output"
  pandoc --self-contained $input -o $output
  echo "Done"
else
  echo "Nothing to update, waiting..."
fi
