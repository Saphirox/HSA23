## Current setup
- Near 27 000 000 records in db (users table)
- Has 1 primary and 2 secondary indexes
- Docker setup: 16 Gi memory, 12 cors
- Docker-compose contains all scripts

## Notes
- CDP and Reverse Delta are not implemented. 
The reason is CDP uses continuous byte transfer to backup so backup time is minimal. So recovery time is the same as for full backup.
The drawback is unablity to rollback at the specific point of time 

## Experiments

### Notes:
- every increment have 2 million records for Differential and Incremental backup. In total all final backups has the same number of records
- Differential and incremental backups have 2 increments 

| Type         | Backup (seconds)              | Rollback (seconds) | Space   |
|--------------|-------------------------------|--------------------|---------|
| Full         | 20s                           | 20s                | 3,69 GB |
| Incremental  | 19s + incr1 (7s) + incr2 (8s) | 23s                | 6,4 GB  |
| Differential | 19s + incr1 (7s) + incr2 (7s) | 22s                | 6,6 GB  |

