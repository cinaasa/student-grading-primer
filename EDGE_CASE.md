# Document your edge case here
- To get marks for this section you will need to explain to your tutor:
1) The edge case you identified
2) How you have accounted for this in your implementation

The edge case I found was when there are zero students, my get_stats() Python would crash with an error.

This is because, I have 'average = sum(marks) / len(marks)'. However when there are zero students, len(marks) = 0. 

This results in 'average' being divided by zero. In math you cannot divide by zero, creating an error (ZeroDivisionError).

Because of this, I created an edge case that first checks if any students exist: 'if not students'. If there are no students, my stats page
automatically outputs zero for every statistic. Only after checking that at least one student exists, does it do normal mathematics calculations
to find the statistics for the students.


