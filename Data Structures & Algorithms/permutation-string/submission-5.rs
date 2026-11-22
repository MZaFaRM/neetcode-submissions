impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let m = s1.len();
        let n = s2.len();

        if m > n {
            return false;
        }

        let mut freq: [i16; 26] = [0; 26];
        for char in s1.as_bytes() {
            freq[(char - 97) as usize] += 1;
        }

        let lookup = s2.as_bytes();
        let mut i:usize = 0;
        for j in 0..n {
            let index = (lookup[j] - 97) as usize;
            freq[index] -= 1;
            while freq[index] < 0 {
                freq[(lookup[i] - 97) as usize] += 1;
                i += 1;
            }
            if j - i + 1 == m {
                return true;
            }
        }
        false
    }
}
