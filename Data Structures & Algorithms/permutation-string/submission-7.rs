impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let m = s1.len();
        let n = s2.len();

        if m > n {
            return false;
        }

        let mut freq: [i16; 26] = [0i16; 26];
        for &b in s1.as_bytes() {
            freq[(b - b'a') as usize] += 1;
        }

        let lookup = s2.as_bytes();
        let mut i = 0;
        for (j, &b) in lookup.iter().enumerate() {
            let idx = (&b - b'a') as usize;
            freq[idx] -= 1;
            while freq[idx] < 0 {
                freq[(lookup[i] - b'a') as usize] += 1;
                i += 1;
            }
            if j + 1 - i == m {
                return true;
            }
        }
        false
    }
}
