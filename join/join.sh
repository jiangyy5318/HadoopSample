
$ hadoop streaming /
  -D stream.reduce.output.field.separator=, /
  -D stream.num.reduce.output.key.fields=4 /
  -D map.output.key.field.separator=, /
  -D num.key.fields.for.partition=2 /
  -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner /
  -input /app/test/test.txt  /
  -output /app/test/test_result /
  -mapper ./mapper.sh  /
  -reducer ./reducer.sh /
  -file mapper.sh /
  -file reducer.sh /
  -jobconf mapre.job.name="sep_test"