package com.example.buildup.data;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class AllImagesDesign {
    @SerializedName("id")
    @Expose
    private Integer id;
    @SerializedName("Image")
    @Expose
    private String image;
    @SerializedName("DesignId")
    @Expose
    private Integer designId;

    public Integer getId() {
        return id;
    }

    public String getImage() {
        return image;
    }

    public Integer getDesignId() {
        return designId;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public void setDesignId(Integer designId) {
        this.designId = designId;
    }
}
