#merge sort
def merge(arr,low,high):
  mid=(low+high)//2
  lf=arr[low:mid+1]
  rg=arr[mid+1:high+1]
  r=0
  l=0
  sort=low
  while l<len(lf) and r<len(rg):
    if lf[l]<=rg[r]:
      arr[sort]=lf[l]
      l=l+1
    else:
      arr[sort]=rg[r]
      r=r+1
    sort=sort+1
  while l<len(lf):
    arr[sort]=lf[l]
    sort=sort+1
    l=l+1
  while r<len(rg):
    arr[sort]=rg[r]
    sort=sort+1
    r=r+1
def ms(arr,low,high):
  if low>=high:
    return
  mid=(low+high)//2
  ms(arr,low,mid)
  ms(arr,mid+1,high)
  merge(arr,low,high)
arr=[15,20,5,30,45,17,40,25,31]
low=0
high=len(arr)-1
ms(arr,low,high)
print(arr)
