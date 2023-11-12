def max_subarray(nums,current_sum):
      for i in range(len(nums)):
         current_sum += nums[i]

         if current_sum > max_sum:
             max_sum = current_sum
             start = current_start
             end = i

         if current_sum < 0:
             current_sum = 0
             current_start = i + 1

      return nums[start:end + 1]


numbers_list = [-1, -2, -1, -5, 2, 1, -4]
result =max_subarray(numbers_list,nums)
print(result)