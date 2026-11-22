func hasDuplicate(nums []int) bool {
	type empty = struct{}
    seen := make(map[int]empty, len(nums))
	for _, v := range nums {
		if _, ok := seen[v]; ok {
			return true
		}
		seen[v] = empty{}
	}
	return false
}
