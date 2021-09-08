from django.urls import reverse
from rest_framework.test import APITestCase

class LenderTests(APITestCase):
    fixtures = ['lenders.json']

    def test_list_lenders(self):
        pass

    def test_create_lender(self):
        data = {
            "name": "Tommy Richard Nguyen",
            "code": "TRN",
            "upfront_commission_rate": 1.36,
            "trial_commission_rate": 1.10,
            "active": True
        }
        url = reverse("manage_lenders:create_lender")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], "Tommy Richard Nguyen")
        self.assertEqual(response.data['code'], "TRN")
        self.assertEqual(response.data['upfront_commission_rate'], 1.36)
        self.assertEqual(response.data['trial_commission_rate'], 1.10)
        self.assertEqual(response.data['active'], True)

    def test_get_lender(self):
        url = reverse("manage_lenders:get_lender", kwargs={"pk": 1})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, 200)

    def test_update_lender(self):
        url = reverse("manage_lenders:update_lender", kwargs={"pk": 2})
        
        patch_data = {
            "upfront_commission_rate": 0.96,
            "trial_commission_rate": 1.34,
        }
        patch_response = self.client.patch(url, patch_data, format="json")
        self.assertEqual(patch_response.status_code, 200)
        self.assertEqual(patch_response.data['name'], "Kathryn Ruth Stephenson")
        self.assertEqual(patch_response.data['code'], "KRS")
        self.assertEqual(patch_response.data['upfront_commission_rate'], 0.96)
        self.assertEqual(patch_response.data['trial_commission_rate'], 1.34)
        self.assertEqual(patch_response.data['active'], False)

        put_data = {
            "name": "Tommy Richard Nguyen",
            "code": "TRN",
            "upfront_commission_rate": 1.36,
            "trial_commission_rate": 1.10,
            "active": True
        }
        put_response = self.client.put(url, put_data, format="json")
        self.assertEqual(put_response.status_code, 200)
        
        bad_put_response = self.client.put(url, patch_data, format="json")
        self.assertEqual(bad_put_response.status_code, 400)


    def test_delete_lender(self):
        url = reverse("manage_lenders:delete_lender", kwargs={"pk": 3})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_bulk_csv_upload(self):
        pass

    def test_bulk_csv_download(self):
        pass
    