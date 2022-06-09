from transformers.models import Transformer
import csv


def run():
    with open(r'transformers/tf_data_section.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Transformer.objects.all().delete()

        for row in reader:
            print(row)

            _, transformer = Transformer.objects.get_or_create(
                transf_loc=row[0],
                sku=row[1],
                primary_voltage=row[2],
                size_kva=row[3],
                transformer_age=row[4],
                customers=row[5],
                percent_lol=row[6],
                consecutive_months_overloaded=row[7],
                loss_of_life=row[8],
                max_overload=row[9],
                life_expectancy_at_conditions=row[10],
                date_max_overload=row[11],
                loading_flags=row[12],
            )

