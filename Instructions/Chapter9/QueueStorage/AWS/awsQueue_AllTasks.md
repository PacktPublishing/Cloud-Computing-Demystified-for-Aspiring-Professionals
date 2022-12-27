# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 9 Configuring Storage Resources for Resiliency
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Configure SQS in AWS

1.	Sign in to the AWS Management Console (https://console.aws.amazon.com/console/).

3.	In the AWS management console, use the search field, enter Queue, and then select Queue.

5.	Select Create queue.

7.	In the Create queue page, select FIFO.

9.	Enter a unique name for your queue with the suffix .fifo.

11.	Select Create Queue.

13.	After your queue is created, select Queues, and then select your queue.

15.	Select Actions from the top menu, and then select Send and receive messages.

17.	Enter message1 in the message body, and enter a message group ID.

19.	Select Send message.

21.	Upon success, select View details to display the sent message.
