/////////////////////////////// Question No. 1 /////////////////////////////////
#include<stdio.h>

int w_time(int q[][3],int n);
int minimumBurstAndArrival(int copyq[][3],int n);
void showDetails(int r[][3],int ct[],int wt[],int tat[],int n);
int minBurst(int copyq[][3],int n);

int main()
{
  int n;

  printf("Enter the number of processes to be processed:\n");
  scanf("%d",&n);

  int p[n][3];

  for(int i=0;i<n;++i)
    p[i][0]=i+1;

  for(int i=0;i<n;++i)
  {

    printf("Enter Burst Time and Arrival Time for Process %d:", i+1);
    scanf("%d %d",&p[i][1],&p[i][2]);
    if(p[i][2]==0)
    {
      printf("Arrival Time can't be Zero. Prcess Discarded!!!!!\n\n");
      --i;
      n=n-1;
    }
  }
  printf("\n\n");
  int t=w_time(p,n);

  printf("\nTotal time taken by Processor for computation is:%d\n\n",t);

}

int w_time(int q[][3],int n)
{
    int copyp[10][3];

    for(int i=0;i<n;++i)
    {
      copyp[i][0]=q[i][0];
      copyp[i][1]=q[i][1];
      copyp[i][2]=q[i][2];
      //printf("%d  %d  %d \n",copyp[i][0],copyp[i][1],copyp[i][2]);
    }


    int wt[50]={0},tat[50]={0},i=0,j=0,k=0,t=0,shortest=0,tot=0,ct[50]={0},min;

    shortest=minimumBurstAndArrival(copyp,n);
    min=copyp[shortest][2];

    int max=copyp[0][2];

    for(int i=0;i<n;++i)
    {
      tot=tot+copyp[i][1];
      if(max<copyp[i][2])
        max=copyp[i][2];
    }
      //printf("%d\n",tot);
    t=min;
    for(i=min;i<(tot+min);++i)
    {

      --copyp[shortest][1];
      ++t;

      if(copyp[shortest][1]==0)
      {
        ct[shortest]=t;
        copyp[shortest][1]=copyp[shortest][2]=32767;
        if(t>=max)
        shortest=minBurst(copyp,n);
        else
        shortest=minimumBurstAndArrival(copyp,n);

        t=t+2;
      }

      //Pre-emption
      if(t<=max)
      { j=0;

        for(int k=0;k<n;++k)
        {
          if(copyp[k][2]<=t)
          {
              if(copyp[shortest][1]>copyp[k][1])
              shortest=k;

          }
        }
      }
    }

    for(i=0;i<n;++i)
    {
      //printf("%d\n",ct[i]);
      tat[i]=ct[i]-q[i][2];
      wt[i]=tat[i]-q[i][1];
    }

    showDetails(q,ct,wt,tat,n);

    return t;
}

int minBurst(int copyq[][3],int n)
{
  int sh=0;
  for(int i=0;i<n;++i)
  {
    if(copyq[sh][1]>copyq[i][1])
    sh=i;
  }
  return sh;
}




int minimumBurstAndArrival(int copyq[][3],int n)
{
  int min=copyq[0][2];
  int sh=0;

  for(int i=0;i<n;++i)
  {

    if(copyq[i][2]<min)
    {
      min=copyq[i][2];
      sh=i;
    }

    if(min==copyq[i][2])
    {
      if(copyq[i][1]<copyq[sh][1])
        sh=i;
    }
  }
  return sh;
}

void showDetails(int r[][3],int ct[],int wt[],int tat[],int n)
{
  printf("Proc No.    BT       AT       CT       WT       TAT\n");

  int sumwt=0,sumtat=0;

  for(int i=0;i<n;++i)
  {
    printf("  %d         %0.2d       %0.2d       %0.2d       %0.2d       %0.2d\n",r[i][0],r[i][1],r[i][2],ct[i],wt[i],tat[i]);
    sumwt=sumwt+wt[i];
    sumtat=sumtat+tat[i];
  }

  float a = (float)sumwt/n;
  float b = (float)sumtat/n;

  printf("\nAverage Waiting Time is: %0.2f\n",a);
  printf("\nAverage Turn Around Time is: %0.2f \n",b);

}
