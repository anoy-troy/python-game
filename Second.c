////////////////////////// Question No. 2 ////////////////////////////
#include<stdio.h>
int main()
{
  int a,total_d=0;
  //int queue[9]={86,1470,913,1774,948,1509,1022,1750,130};
  //int head=143;

  int queue[5000];
  int head;

  printf("\n\n*****  Implementing FCFS Disc-Scheduling Algorithm  *****\n\n");

  printf("Enter no. of requests pending in the queue for processing:");
  scanf("%d",&a);

  printf("\nEnter the cylinder no. for corresponding requests in FCFS order \n");

  for(int i=0;i<a;++i)
  scanf("%d",&queue[i]);

  printf("\nEnter current position of disc arm :");
  scanf("%d",&head);

  for(int i=0;i<a;++i)
  {
    if((queue[i]-head)>0)
      total_d=total_d + queue[i] - head;
    else
      total_d=total_d - queue[i] + head;

    head=queue[i];
  }

  printf("\n\nThe total distance moved by disc arm is:%d\n\n",total_d);

  return 0;
}
