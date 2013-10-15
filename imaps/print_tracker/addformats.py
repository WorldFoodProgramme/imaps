from odep.models import Format

formats = ('A0','A1','A2','A3','A4','A5')

for f in formats:
	Format.objects.create(name = f)