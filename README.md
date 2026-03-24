# bREach
bREach (the RE is intentional, it stands for Reverese Engineering) is a modular offensive security framework built for CTF challenges and beyond.

This project is as much a learning vehicle as it is a tool. Built across multiple languages (bash, Python, C, and whatever comes next), each module reflects a skill being developed in parallel. Expect it to grow organically.

The long term vision is a lightweightm, self-contained framework for tackling CTF challenges across all categories, with potential CVE POCs added as knowledge deepens.

## Current State 

Early development. The foundation is being laid.

**Modules**
- `recon/netscan`:TCP/UDP network scanner (Rustscan + Nmap wrapper)
- `crypto/rsa`: Basic RSA challenge solver (small modulus only, for now)

## Roadmap

- Core dispatcher
- Session/state management per target
- Expanded module categories: Web, Exploitation, Forensics
- C modules as C knowledge grows

## Author

hyprcall -- CTF player, aspiring security researcher, perpetual student.

