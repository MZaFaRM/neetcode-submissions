func checkInclusion(s1 string, s2 string) bool {
    m := len(s1)
	n := len(s2)
	if m > n {
		return false
	}
	freq := [26]int{}
	for i := range m {
		freq[s1[i] - 'a']++
	}

	i := 0
	for j := range s2 {
		idx := s2[j] - 'a'
		freq[idx]--
		for freq[idx] < 0 {
			freq[s2[i] - 'a']++
			i++
		}
		if j - i + 1 == m {
			return true
		}
		
	}
	return false

}
