def equalizeSize(teamSize, k)
  maxcount = 0
  element_having_max_freq = 0
  n = teamSize.length

  for i in (0..n)
    count = 0
    for j in (0..n)
      if teamSize[i] == teamSize[j]
        count += 1
      end
    if count > maxcount
      maxcount = count
      element_having_max_freq = teamSize[i]
    end
    end
  end

  if k < teamSize.length
    counter_of_done_reductions = 0
    for x in teamSize
      if (x > element_having_max_freq) && (counter_of_done_reductions < k)
        counter_of_done_reductions += 1
      end
    end
    result = maxcount + counter_of_done_reductions
    return result
  else
    return teamSize.length
  end
end

array1 = [1,2,3,2,4]
k1 = 2 # output should be 4
puts equalizeSize(array1,k1)

array2 = [1,2,3,5,4,6,7]
k2 = 10 #output should be 7
puts equalizeSize(array2,k2)

array3 = [1,8,3,7]
k3 = 1 #output should be 2
puts equalizeSize(array3,k3)
