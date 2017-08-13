# HadoopSample


Hadoop streaming 使用

hadoop过程如下：
Input->Map->mapsort->Patition->mergesort->Reduce->Output

HADOOP如何进行Join操作

-D stream.map.output.field.separator ：设置 map 输出中 key 和 value 的分隔符 
-D stream.num.map.output.key.fields ：设置 map 程序分隔符的位置，该位置之前的部分作为 key，之后的部分作为 value
-D map.output.key.field.separator : 设置 map 输出分区时 key 内部的分割符 
-D mapreduce.partition.keypartitioner.options : 指定分桶时，key 按照分隔符切割后，其中用于分桶 key 所占的列数
（配合 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner 使用）
-D stream.reduce.output.field.separator ：设置 reduce 输出中 key 和 value 的分隔符 
-D stream.num.reduce.output.key.fields ：设置 reduce 程序分隔符的位置,,,,, 这个有什么意义.
mapreduce.partition.keypartitioner.options=-k1,2
-D stream.memory.limit=8000    #内存上限
-D mapred.job.reduce.memory.mb=8000    #内存上限



注意事项：
1. -file使用，mapper或者reduce程序不需要事先部署在Hadoop集群的任意一台机器上，我们仅仅需要在提交Streaming作业的时候指定-file参数，这样Hadoop会自动将这些文件分发到集群指定可执行文件之外，我们还可以打包 mapper 或者 Reduce 程序会用到的文件（包括目录，配置文件等）
2. 只输出map,
-D mapreduce.job.reduces=0
-reducer NONE
两者是或的关系,任何一项设置会导致Map/Reduce框架不会启动Reduce类型的task。map task的输出就是作业的最终结果输出.
3. map支持多输入(join使用),一般我们可以通过内容的格式,比如一种是5个\t分割,一个是3个\t分割.也可以通过文件源区分具体为os.ENVIRON["map_input_file"]，shell可以直接使用match("'${map_input_file}'","aaaaa")
4. reducer多路输出reduce
reducer 可以有多路输出，但基于非常初级的封装，产生的reduce输出文件为part-xxxxx-X文件，其中X是A-Z的字母之一，使用方法如下在命令行中启用多路输出，多路输出一般在$line后面加#X(X表示A-Z),多路输出也只能输出26路;另外多路输出需要配置-outputformat org.apache.hadoop.mapred.lib.SuffixMultipleTextOutputFormat
#或
-outputformat org.apache.hadoop.mapred.lib.SuffixMultipleSequenceFileOutputFormat
5.  partitioner，map的输出结果需要分发到各个reducer中，partitioner就是控制分发的策略的。默认情况下，按照map结果的第一个域作为key（以\t分隔，使用默认的HashPartitioner），某些情况下，我们需要将第一个域的一部分作为key分发到同一个reducer中。Hadoop 提供了一个非常实用的partitioner类KeyFieldBasedPartitioner，通过配置相应的参数就可以使用。通过KeyFieldBasedPartitioner可以方便地实现二次排序。
6.  传递环境变量
HADOOP_HOME      计算节点上配置的Hadoop路径
LD_LIBRARY_PATH  计算节点上加载库文件的路径列表
PWD              当前工作目录
dfs_block_size   当前设置的HDFS文件块大小
map_input_file   mapper正在处理的输入文件路径
mapred_job_id    作业ID
mapred_job_name  作业名
mapred_tip_id    当前任务的第几次重试
mapred_task_id   任务ID
mapred_task_is_map 当前任务是否为map
mapred_output_dir  计算输出路径
mapred_map_tasks   计算的map任务数 
mapred_reduce_tasks计算的reduce任务数
7. 等待完善
Hadoop Aggregate Package
Hadoop 中有一个类 Aggregate，Aggregate 提供了一个特定的 reduce 类和 combiner 类，以及一些对 reduce 输出的聚合函数，例如 sum、min、max等等。为了使用 Aggregate，我们只需要定义 -reducer aggregate参数
 
 FieldSelectionMapReduce 自定义列.