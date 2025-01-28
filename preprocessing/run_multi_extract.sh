for FILE in *.tar.gz; do
    echo ${FILE} | cut -d '/' -f 3
    sbatch -A  project_name -n 1 -t 5:00:00 --wrap="python extract_conversion.py  $(echo ${FILE}|cut -d '/' -f 3)" 
    sleep 1 # pause to be kind to the scheduler
done
