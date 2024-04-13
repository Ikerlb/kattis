use std::io::{self, Write, BufWriter};

fn main() -> io::Result<()> {
    let stdout = io::stdout();
    let mut writer = BufWriter::new(stdout);
    writeln!(writer, "VELKOMIN!");
    return Ok(());
}
